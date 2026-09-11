from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c604b45a-0d6e-55c3-a9e8-600fd9e7f7dd',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name',
    display_name='Drapion',
    searchable_by=['Drapion', 'Stage 1', 'Drapion'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name',
    family_id=451,
    abilities=[
        Attack(
            title='Toxic Fang',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Poisoned. Put 2 damage counters instead of 1 on that Pokémon between turns.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Land Crush',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
