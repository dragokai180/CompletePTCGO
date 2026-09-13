# Gallery print swsh12pt5gg/GG45; artwork is downloaded by the installer.
from spirit.game.card_effects.galleries import max_drain, ProtectiveDNAPassive
from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bddc8102-8e12-51b4-9d9e-fe56dc4ab739',
    key='CZ',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVMAX.Name',
    display_name='Deoxys VMAX',
    searchable_by=['Deoxys VMAX', 'VMAX', 'DeoxysVMAX'],
    subtypes=['VMAX'],
    collector_number=205,
    set_code='CZ',
    regulation_mark='F',
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'GG45'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name',
    family_id=386,
    abilities=[
        Ability(
            title='Protective DNA',
            game_text="All of your Pokémon take 30 less damage from attacks from your opponent's Pokémon VSTAR (after applying Weakness and Resistance).",
            passive=ProtectiveDNAPassive(),
        ),
        Attack(
            title='Max Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=max_drain,
        ),
    ],
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG45"}
