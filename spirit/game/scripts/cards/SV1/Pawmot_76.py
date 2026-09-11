from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b5a77627-007c-5d52-a28b-8cd588df8afc',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name',
    display_name='Pawmot',
    searchable_by=['Pawmot', 'Stage 2', 'Pawmot'],
    subtypes=['Stage 2'],
    collector_number=76,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name',
    family_id=921,
    abilities=[
        Ability(
            title='Electrogenesis',
            game_text='Once during your turn, you may search your deck for a Basic Lightning Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Electro Paws',
            game_text='Discard all Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=standard_attack,
        ),
    ],
)
