from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ff542ab8-f53c-5143-a4b7-03dd1101c173',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swalot.Name',
    display_name='Swalot',
    searchable_by=['Swalot', 'Stage 1', 'Swalot'],
    subtypes=['Stage 1'],
    collector_number=58,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name',
    family_id=316,
    abilities=[
        Attack(
            title='Amnesia',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Swallow Up',
            game_text="If, before doing damage, your opponent's Active Pokémon has less remaining HP than this Pokémon, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
