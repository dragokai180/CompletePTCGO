from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34bc76b1-3bb0-5d9e-9b97-7ebda726e9ce',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name',
    display_name='Groudon',
    searchable_by=['Groudon', 'Basic', 'Groudon'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=383,
    abilities=[
        Attack(
            title='Break Ground',
            game_text="This attack also does 20 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 5},
            damage=250,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
