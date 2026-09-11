from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='29841ba1-bb1c-534e-ad96-d4239b381acc',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name',
    display_name='Luvdisc',
    searchable_by=['Luvdisc', 'Basic', 'Luvdisc'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=370,
    abilities=[
        Attack(
            title='Matching',
            game_text='Search your deck for up to 2 Supporter cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
