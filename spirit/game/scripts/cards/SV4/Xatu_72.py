from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0c901957-88f8-5b85-a7ba-f8510d0828e2',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name',
    display_name='Xatu',
    searchable_by=['Xatu', 'Stage 1', 'Xatu'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name',
    family_id=177,
    abilities=[
        Ability(
            title='Clairvoyant Sense',
            game_text='Once during your turn, you may attach a Basic Psychic Energy card from your hand to 1 of your Benched Pokémon. If you attached Energy to a Pokémon in this way, draw 2 cards.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Super Psy Bolt',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
