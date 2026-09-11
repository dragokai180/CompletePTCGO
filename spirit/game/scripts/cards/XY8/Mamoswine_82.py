from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6988e9da-fd28-5a5f-aae6-26263ed0d768',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name',
    display_name='Mamoswine',
    searchable_by=['Mamoswine', 'Stage 2', 'Mamoswine'],
    subtypes=['Stage 2'],
    collector_number=82,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name',
    family_id=220,
    abilities=[
        Ability(
            title='Thick Fat',
            game_text="Any damage done to this Pokémon by attacks from your opponent's Fire or Water Pokémon is reduced by 30 (after applying Weakness and Resistance).",
            passive=standard_passive("Any damage done to this Pokémon by attacks from your opponent's Fire or Water Pokémon is reduced by 30 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Primordial Boom',
            game_text='If you have a Stadium card in play, this attack does 40 more damage. If your opponent has a Stadium card in play, heal 40 damage from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
