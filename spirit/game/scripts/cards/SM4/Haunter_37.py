from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='434dc6d8-6496-51eb-b61b-e0ae778a4cb5',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    display_name='Haunter',
    searchable_by=['Haunter', 'Stage 1', 'Haunter'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name',
    family_id=92,
    abilities=[
        Attack(
            title='Pain Amplifier',
            game_text="Put 2 damage counters on each of your opponent's Pokémon that has any damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
