# Gallery print swsh12pt5gg/GG46; artwork is downloaded by the installer.
from spirit.game.card_effects.galleries import psychic_javelin, star_force
from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4c76c5a-932f-5200-8390-2ae28f998560',
    key='CZ',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVSTAR.Name',
    display_name='Deoxys VSTAR',
    searchable_by=['Deoxys VSTAR', 'VSTAR', 'DeoxysVSTAR'],
    subtypes=['VSTAR'],
    collector_number=206,
    set_code='CZ',
    regulation_mark='F',
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'GG46'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name',
    family_id=386,
    abilities=[
        Attack(
            title='Psychic Javelin',
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon V. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=psychic_javelin,
        ),
        Attack(
            title='Star Force',
            vstar=True,
            game_text="This attack does 60 damage for each Energy attached to both Active Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator='x',
            effect=star_force,
        ),
    ],
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG46"}
