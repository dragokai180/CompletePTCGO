from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3eabc5f4-eb6b-53ee-a5c3-912cb1fd42e8',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name',
    display_name='Togekiss',
    searchable_by=['Togekiss', 'Stage 2', 'Togekiss'],
    subtypes=['Stage 2'],
    collector_number=85,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name',
    family_id=175,
    abilities=[
        Ability(
            title='Precious Gift',
            game_text='Once at the end of your turn (after your attack), you may use this Ability. Draw cards until you have 8 cards in your hand.',
            effect=standard_ability,
            trigger=Triggers.END_OF_TURN,
        ),
        Attack(
            title='Power Cyclone',
            game_text='Move an Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
