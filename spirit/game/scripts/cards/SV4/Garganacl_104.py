from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='41e62809-769f-5f1f-9366-6f16cc6bf89b',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name',
    display_name='Garganacl',
    searchable_by=['Garganacl', 'Stage 2', 'Garganacl'],
    subtypes=['Stage 2'],
    collector_number=104,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name',
    family_id=932,
    abilities=[
        Ability(
            title='Energizing Rock Salt',
            game_text='Once during your turn, you may attach a Basic Fighting Energy card from your discard pile to 1 of your Pokémon. If you attached Energy to a Pokémon in this way, heal 30 damage from that Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Land Crush',
            cost={PokemonTypes.FIGHTING: 3},
            damage=140,
        ),
    ],
)
