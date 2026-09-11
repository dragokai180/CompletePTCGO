from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f1be7ceb-b271-59d0-bbb5-7463f7538c21',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name',
    display_name='Slowbro',
    searchable_by=['Slowbro', 'Stage 1', 'Slowbro'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=79,
    abilities=[
        Attack(
            title='Amnesia',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Facade',
            game_text='If this Pokémon is Burned or Poisoned, this attack does 80 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
