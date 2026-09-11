from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='46ed545f-af43-56fd-8a97-5b50ae3a418e',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    display_name='Doublade',
    searchable_by=['Doublade', 'Stage 1', 'Doublade'],
    subtypes=['Stage 1'],
    collector_number=48,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    family_id=679,
    abilities=[
        Attack(
            title='Curse of the Blade',
            game_text="Put 3 damage counters on each of your opponent's Pokémon that has a Pokémon Tool card attached to it.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
