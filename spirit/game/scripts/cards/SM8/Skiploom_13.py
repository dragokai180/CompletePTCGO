from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b92c020e-e7fd-5584-9e52-d064a7dec3b6',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name',
    display_name='Skiploom',
    searchable_by=['Skiploom', 'Stage 1', 'Skiploom'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name',
    family_id=187,
    abilities=[
        Ability(
            title='Floral Path to the Sky',
            game_text='Once during your turn (before your attack), you may search your deck for Jumpluff, put this Pokémon and all cards attached to it in the Lost Zone, and put that Jumpluff in its place. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
