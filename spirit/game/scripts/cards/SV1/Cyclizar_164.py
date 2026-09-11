from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a6eb302e-2847-54bd-9f42-6257d40a4e55',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name',
    display_name='Cyclizar',
    searchable_by=['Cyclizar', 'Basic', 'Cyclizar'],
    subtypes=['Basic'],
    collector_number=164,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=967,
    abilities=[
        Attack(
            title='Touring',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Speed Attack',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
