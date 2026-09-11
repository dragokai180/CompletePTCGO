from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='015d4f00-4dae-5e8b-8920-6d4eed44484a',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name',
    display_name='Oinkologne',
    searchable_by=['Oinkologne', 'Stage 1', 'Oinkologne'],
    subtypes=['Stage 1'],
    collector_number=157,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name',
    family_id=915,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Leg Stomp',
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
