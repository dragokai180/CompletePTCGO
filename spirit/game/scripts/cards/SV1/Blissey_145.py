from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7eb6223c-9ec2-53d5-a297-2997bc1ecd6b',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name',
    display_name='Blissey',
    searchable_by=['Blissey', 'Stage 1', 'Blissey'],
    subtypes=['Stage 1'],
    collector_number=145,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    family_id=113,
    abilities=[
        Ability(
            title='Busybody Nurse',
            game_text='Once during your turn, you may use this Ability. Your Active Pokémon recovers from all Special Conditions.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Happy Cyclone',
            game_text='Move all Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
