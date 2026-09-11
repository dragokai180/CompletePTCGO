from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5ba0b625-ba93-54c4-88d4-729ddc2359cf',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name',
    display_name='Delphox',
    searchable_by=['Delphox', 'Stage 2', 'Delphox'],
    subtypes=['Stage 2'],
    collector_number=17,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name',
    family_id=653,
    abilities=[
        Ability(
            title='Mystical Torch',
            game_text="Once during your turn (before your attack), you may leave your opponent's Active Pokémon Burned.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Fire Spin',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
