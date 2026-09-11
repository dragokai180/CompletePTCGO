from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='637e454f-b5db-5621-995d-bac86e846b99',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ArmoredMewtwo.Name',
    display_name='Armored Mewtwo',
    searchable_by=['Armored Mewtwo', 'Basic', 'ArmoredMewtwo'],
    subtypes=['Basic'],
    collector_number=228,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=150,
    abilities=[
        Attack(
            title='Psychic Raid',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
