from collections import deque
from re import findall


class Blueprint:
    def __init__(self, ore_bot, clay_bot, obsidian_bot, geode_bot):
        self.ore_bot = ore_bot
        self.clay_bot = clay_bot
        self.obsidian_bot = obsidian_bot
        self.geode_bot = geode_bot
        self.iter = [self.ore_bot, self.clay_bot, self.obsidian_bot, self.geode_bot]
        self.n = 0

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.iter):
            self.n += 1
            return self.iter[self.n - 1]
        raise StopIteration


class Bot:
    def __init__(self, price, production):
        self.production = production
        self.price = price

    def __repr__(self):
        return 'Bot produces: \n' + str(self.production) + 'Bot costs: \n' + str(self.price)


class Wallet:
    def __init__(self, ore=0, clay=0, obsidian=0, geode=0):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __contains__(self, item):
        return self.ore >= item.ore \
               and self.clay >= item.clay \
               and self.obsidian >= item.obsidian \
               and self.geode >= item.geode

    def __add__(self, other):
        return Wallet(
            self.ore + other.ore,
            self.clay + other.clay,
            self.obsidian + other.obsidian,
            self.geode + other.geode
        )

    def __sub__(self, other):
        return Wallet(
            self.ore - other.ore,
            self.clay - other.clay,
            self.obsidian - other.obsidian,
            self.geode - other.geode
        )

    def __repr__(self):
        return (f'  Ore: {self.ore}\n' if self.ore else '') + \
               (f'  Clay: {self.clay}\n' if self.clay else '') +\
               (f'  Obsidian: {self.obsidian}\n' if self.obsidian else '') + \
               (f'  geode: {self.geode}\n' if self.geode else '')


class Game:
    def __init__(self, blueprint, rounds):
        self.blueprint = blueprint
        self.wallet = Wallet(0, 0, 0, 0)
        self.rounds = rounds
        self.bots = []
        self.round = 0
        self.in_progress = [blueprint.ore_bot]

    def purchase_bot(self, bot):
        self.wallet -= bot.price
        self.in_progress.append(bot)

    def end(self):
        self.mine()

    def affordable_options(self):
        return [option for option in self.blueprint if option.price in self.wallet]

    def mine(self):
        prod = Wallet()
        for bot in self.bots:
            prod += bot.production

        self.wallet += prod

    def __iter__(self):
        return self

    def __next__(self):
        if self.round == self.rounds:
            self.end()
            raise StopIteration
        self.round += 1
        self.mine()
        self.bots.extend(self.in_progress)
        self.in_progress = []
        return self


def read():
    blueprints = []
    with open('input', 'r') as file:
        for line in file:
            _, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = (int(x) for x in findall('[0-9]+', line))
            blueprints.append(
                Blueprint(
                    Bot(
                        Wallet(ore=ore_ore),
                        Wallet(ore=1)
                    ),
                    Bot(
                        Wallet(ore=clay_ore),
                        Wallet(clay=1)
                    ),
                    Bot(
                        Wallet(ore=obs_ore, clay=obs_clay),
                        Wallet(obsidian=1)
                    ),
                    Bot(
                        Wallet(ore=geo_ore, obsidian=geo_obs),
                        Wallet(geode=1)
                    )
                )
            )
    return blueprints


def part1():
    blueprints = read()
    game_length = 24
    total_quality = 0
    explored_nodes = 0
    for no, blueprint in enumerate(blueprints):
        local_best = -1, 0
        q = deque([([10 for _ in range(game_length)], 0)])
        k = 0
        while q:
            k += 1
            game = Game(blueprint, game_length)
            inp_seq, explored = q.popleft()
            for i, round in enumerate(game):
                options = round.affordable_options()
                if explored < i and len(options) > 0 and inp_seq[i] == 10:
                    for j in range(0, len(options)):
                        new_seq = inp_seq[:i] + [len(options) - j - 2] + [10 for _ in range(game_length - i - 1)]
                        q.append((new_seq, i))
                if inp_seq[i] > -1 and len(options) > 0:
                    round.purchase_bot(options[min(inp_seq[i], len(options) - 1)])
            local_best = max(local_best, (game.wallet.geode, k))
            if k > 10_000:
                break
        explored_nodes += local_best[1]
        total_quality += local_best[0] * (no + 1)
    print()
    print(f'Explored {explored_nodes} nodes')
    return total_quality


def part1_game():
    blueprints = read()
    for blueprint in blueprints:
        game = Game(blueprint, 24)
        for round_no, round in enumerate(game):
            print(f'######################## ROUND {round.round: <2} #######################')
            print('Number of bots', len(round.bots))
            print('Current wallet:')
            print(game.wallet)
            print('Affordable options')
            options = round.affordable_options()
            for i, option in enumerate(options):
                print(f'{i + 1}) ')
                print(option)

            pick = input('> ')
            if pick:
                round.purchase_bot(options[int(pick) - 1])

            print(f'---------------------------------------------------------')
        exit()

    return


def part2():
    blueprints = read()[:3]
    game_length = 32
    total_quality = 1
    explored_nodes = 0
    for no, blueprint in enumerate(blueprints):
        local_best = -1, 0
        q = deque([([10 for _ in range(game_length)], 0)])
        k = 0
        while q:
            k += 1
            game = Game(blueprint, game_length)
            inp_seq, explored = q.popleft()
            for i, round in enumerate(game):
                options = round.affordable_options()
                if explored < i and len(options) > 0 and inp_seq[i] == 10:
                    for j in range(0, len(options)):
                        new_seq = inp_seq[:i] + [len(options) - j - 2] + [10 for _ in range(game_length - i - 1)]
                        q.append((new_seq, i))
                if inp_seq[i] > -1 and len(options) > 0:
                    round.purchase_bot(options[min(inp_seq[i], len(options) - 1)])
            local_best = max(local_best, (game.wallet.geode, k))
            if k > 3_000:
                break
        explored_nodes += local_best[1]
        total_quality *= local_best[0]

    print(f'Explored {explored_nodes} nodes')
    return total_quality


if __name__ == '__main__':
    print(f'Part 1:', part1())
    print(f'Part 2:', part2())
