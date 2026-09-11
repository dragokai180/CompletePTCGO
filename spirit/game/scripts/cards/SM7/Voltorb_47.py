from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='edda0f10-395c-590b-ad18-c30a41a9bb4f',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    display_name='Voltorb',
    searchable_by=['Voltorb', 'Basic', 'Voltorb'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=100,
    abilities=[
        Ability(
            title='Floating Electrons',
            game_text='If this Pokémon has any Energy attached to it, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Energy attached to it, it has no Retreat Cost.'),
        ),
        Attack(
            title='Thunder Shock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
