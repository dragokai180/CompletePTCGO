from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5cc1a896-40a8-5072-a437-9454f9c4e2a5',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name',
    display_name='Heliolisk',
    searchable_by=['Heliolisk', 'Stage 1', 'Heliolisk'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name',
    family_id=695,
    abilities=[
        Ability(
            title='Dry Skin',
            game_text="Any damage done to this Pokémon by an attack from 1 of your opponent's Water Pokémon is reduced by 30 (after applying Weakness and Resistance).",
            passive=standard_passive("Any damage done to this Pokémon by an attack from 1 of your opponent's Water Pokémon is reduced by 30 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Hyper Beam',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
