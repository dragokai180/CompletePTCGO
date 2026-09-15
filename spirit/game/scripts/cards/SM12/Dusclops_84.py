from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c6b424e8-a845-5da9-987b-7ca982818724',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name',
    display_name='Dusclops',
    searchable_by=['Dusclops', 'Stage 1', 'Dusclops'],
    subtypes=['Stage 1'],
    collector_number=84,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name',
    family_id=355,
    abilities=[
        Attack(
            title='Disable',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=standard_attack,
            locks_next_turn=False,
        ),
    ],
)
