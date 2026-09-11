from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f84611cc-0cd0-5516-bf79-3c2ebb4b90da',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name',
    display_name='Flareon',
    searchable_by=['Flareon', 'Stage 1', 'Flareon'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Ability(
            title='Flare Effect',
            game_text='Each of your Stage 1 Pokémon in play is now a Fire Pokémon in addition to its existing types.',
            passive=standard_passive('Each of your Stage 1 Pokémon in play is now a Fire Pokémon in addition to its existing types.'),
        ),
        Attack(
            title='Heat Breath',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
