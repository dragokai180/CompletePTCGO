from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='89a93260-f41b-5d89-8d76-22e5417c5edd',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name',
    display_name='Gengar',
    searchable_by=['Gengar', 'Stage 2', 'Gengar'],
    subtypes=['Stage 2'],
    collector_number=57,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    family_id=92,
    abilities=[
        Ability(
            title='Night Gate',
            game_text='Once during your turn, you may switch your Active Pokémon with 1 of your Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Nightmare',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
