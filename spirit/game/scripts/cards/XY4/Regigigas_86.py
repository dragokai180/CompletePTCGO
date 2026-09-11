from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be1a842b-b1cb-569a-8a8c-f959ae89788d',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name',
    display_name='Regigigas',
    searchable_by=['Regigigas', 'Basic', 'Regigigas'],
    subtypes=['Basic'],
    collector_number=86,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=486,
    abilities=[
        Attack(
            title='Daunt',
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pokémon is reduced by 40 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
        ),
    ],
)
