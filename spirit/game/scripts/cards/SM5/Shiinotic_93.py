from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7c23401d-1ab9-568d-ba28-2ffa24535624',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name',
    display_name='Shiinotic',
    searchable_by=['Shiinotic', 'Stage 1', 'Shiinotic'],
    subtypes=['Stage 1'],
    collector_number=93,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name',
    family_id=755,
    abilities=[
        Ability(
            title='Illuminate',
            game_text='Once during your turn (before your attack), you may search your deck for a Fairy Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Flickering Spores',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
