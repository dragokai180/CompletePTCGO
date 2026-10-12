from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Triggers, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import standard_attack


async def kinesis_before_evolve(ctx):
    evolution = ctx.evolved_pokemon
    if evolution is None or def_for(evolution.archetype_id).display_name != 'M Alakazam-EX':
        ctx.suppress_announce = True
        return
    active = ctx.opponent_active()
    if active is None or not await ctx.ask_yes_no('Use Kinesis?'):
        ctx.suppress_announce = True
        return
    await ctx.deal_damage(20, target=active, apply_modifiers=False,
                          as_counters=True, is_attack=False)
    bench = list(ctx.opponent_bench())
    if bench:
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, 'Choose a Benched Pokémon for Kinesis')
        if target is not None:
            await ctx.deal_damage(30, target=target, apply_modifiers=False,
                                  as_counters=True, is_attack=False)


card = PokemonCardDef(
    guid='27c100c4-04c4-5a4f-b6f5-3c300f41f680',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name',
    display_name='Alakazam-EX',
    searchable_by=['Alakazam-EX', 'Basic', 'EX', 'AlakazamEX'],
    subtypes=['Basic', 'EX'],
    collector_number=25,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=65,
    abilities=[
        Ability(
            title='Kinesis',
            game_text="When you play M Alakazam-EX from your hand to evolve this Pokémon, before it evolves, you may put 2 damage counters on your opponent's Active Pokémon and 3 damage counters on 1 of your opponent's Benched Pokémon.",
            trigger=Triggers.BEFORE_EVOLVE,
            effect=kinesis_before_evolve,
        ),
        Attack(
            title='Suppression',
            game_text="Put 3 damage counters on each of your opponent's Pokémon that has any Energy attached to it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
