from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5a148f75-a697-5bce-af1b-11d16ef2d695',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    display_name='Kakuna',
    searchable_by=['Kakuna', 'Stage 1', 'Kakuna'],
    subtypes=['Stage 1'],
    collector_number=32,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    family_id=13,
    abilities=[
        Attack(
            title='Speed Evolution',
            game_text='Search your deck for a card that evolves from Kakuna and put it onto Kakuna. (This counts as evolving Kakuna.) Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Poison Sting',
            game_text='The Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
