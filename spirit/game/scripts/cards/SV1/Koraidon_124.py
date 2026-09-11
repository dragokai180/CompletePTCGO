from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0e53d49c-dee5-520e-8de4-c4cb5fa5dc2e',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name',
    display_name='Koraidon',
    searchable_by=['Koraidon', 'Basic', 'Koraidon'],
    subtypes=['Basic'],
    collector_number=124,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=1007,
    abilities=[
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
        Attack(
            title='Rampaging Fang',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
