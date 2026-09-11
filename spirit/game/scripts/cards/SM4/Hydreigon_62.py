from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9133ec9a-4f4c-5867-a2a0-6f7fcc8f349c',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name',
    display_name='Hydreigon',
    searchable_by=['Hydreigon', 'Stage 2', 'Hydreigon'],
    subtypes=['Stage 2'],
    collector_number=62,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name',
    family_id=633,
    abilities=[
        Ability(
            title='Weed Out',
            game_text='Once during your turn (before your attack), you may choose 3 of your Benched Pokémon. Then, discard your other Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Dark Destruction',
            game_text="You may discard an Energy from this Pokémon. If you do, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
