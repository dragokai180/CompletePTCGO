from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d7899595-c1ec-54f6-b766-37fe395384b2',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name',
    display_name='Talonflame',
    searchable_by=['Talonflame', 'Stage 2', 'Talonflame'],
    subtypes=['Stage 2'],
    collector_number=96,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    family_id=661,
    # Gale Wings is an opening-placement exception, not a hand action.
    # Declare it directly, including when imported outside the catalog loader.
    setup_as_active=True,
    abilities=[
        Ability(
            title='Gale Wings',
            game_text='If this Pokémon is in your hand when you are setting up to play, you may put it face down as your Active Pokémon.',
        ),
        Attack(
            title='Aero Blitz',
            game_text='Search your deck for up to 2 cards and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
