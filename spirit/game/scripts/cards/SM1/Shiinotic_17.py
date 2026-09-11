from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dfd0ae6e-8e7f-5366-9695-00d5dac401e7',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name',
    display_name='Shiinotic',
    searchable_by=['Shiinotic', 'Stage 1', 'Shiinotic'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name',
    family_id=755,
    abilities=[
        Ability(
            title='Illuminate',
            game_text='Once during your turn (before your attack), you may search your deck for a Grass Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Flickering Spores',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
