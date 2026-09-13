# Gallery print swsh12pt5gg/GG40; artwork is downloaded by the installer.
from spirit.game.card_effects.galleries import icicle_shot, crystal_star
from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3f1d4a3-2beb-5a7d-80ef-8db609327ab9',
    key='CZ',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonVSTAR.Name',
    display_name='Glaceon VSTAR',
    searchable_by=['Glaceon VSTAR', 'VSTAR', 'GlaceonVSTAR'],
    subtypes=['VSTAR'],
    collector_number=200,
    set_code='CZ',
    regulation_mark='F',
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'GG40'}},
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name',
    family_id=471,
    abilities=[
        Attack(
            title='Icicle Shot',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=icicle_shot,
        ),
        Attack(
            title='Crystal Star',
            vstar=True,
            game_text="During your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=crystal_star,
        ),
    ],
)

card.extra_attributes["200790"] = {"type": "string", "value": "GG40"}
