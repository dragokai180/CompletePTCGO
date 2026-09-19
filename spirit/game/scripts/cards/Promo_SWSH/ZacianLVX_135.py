from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='324353f0-3073-5153-9619-fb0efad5580f',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ZacianLVX.Name',
    display_name='Zacian LV.X',
    searchable_by=['Zacian LV.X', 'Level-Up', 'ZacianLVX'],
    subtypes=['Level-Up'],
    collector_number=135,
    set_code='Promo_SWSH',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.LEVELUP,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH135'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name',
    family_id=888,
    abilities=[
        Ability(
            title='Bladed Armament',
            game_text="Damage from this Pokémon's attacks isn't affected by any effects on your opponent's Active Pokémon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Damage from this Pokémon's attacks isn't affected by any effects on your opponent's Active Pokémon."),
        ),
        Attack(
            title='Brave Blade',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=standard_attack,
        ),
    ],
)
