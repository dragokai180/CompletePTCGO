from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='121a4c13-9501-5e3b-83f3-77d9fdd57a83',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name',
    display_name='Froslass',
    searchable_by=['Froslass', 'Stage 1', 'Froslass'],
    subtypes=['Stage 1'],
    collector_number=38,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    family_id=361,
    abilities=[
        Attack(
            title='Spiteful Sigh',
            game_text='Put up to 7 damage counters on this Pokémon. This attack does 20 damage for each damage counter you placed in this way.',
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Icy Wind',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
