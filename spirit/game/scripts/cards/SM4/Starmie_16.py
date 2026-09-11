from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a15c94b9-a741-5319-82c5-46ddd5d8344d',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name',
    display_name='Starmie',
    searchable_by=['Starmie', 'Stage 1', 'Starmie'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    family_id=120,
    abilities=[
        Ability(
            title='Escape',
            game_text='Once during your turn (before your attack), you may shuffle this Pokémon and all cards attached to it into your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
