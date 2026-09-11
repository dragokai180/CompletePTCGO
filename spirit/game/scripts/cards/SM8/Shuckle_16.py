from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d766af80-2f7b-598a-83e2-ace501a6ed18',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name',
    display_name='Shuckle',
    searchable_by=['Shuckle', 'Basic', 'Shuckle'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=213,
    abilities=[
        Ability(
            title='Fresh Squeezed',
            game_text='When you play this Pokémon from your hand onto your Bench during your turn, you may search your deck for up to 3 basic Energy cards and discard them. Then, shuffle your deck.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Energy Drink',
            game_text='Attach 2 basic Energy cards from your discard pile to your Pokémon in any way you like.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
