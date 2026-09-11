from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e0c289b-3971-5c90-897e-3084c2fee77d',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name',
    display_name='Bisharp',
    searchable_by=['Bisharp', 'Stage 1', 'Bisharp'],
    subtypes=['Stage 1'],
    collector_number=135,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name',
    family_id=624,
    abilities=[
        Attack(
            title='Corner',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Strike',
            game_text="This Pokémon can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
