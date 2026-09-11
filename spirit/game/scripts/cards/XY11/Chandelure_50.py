from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='474330c2-b16b-54da-b78d-c6ef27173fd1',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name',
    display_name='Chandelure',
    searchable_by=['Chandelure', 'Stage 2', 'Chandelure'],
    subtypes=['Stage 2'],
    collector_number=50,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name',
    family_id=607,
    abilities=[
        Ability(
            title='Sinister Selection',
            game_text='Once during your turn (before your attack), you may look at the top 2 cards of your deck and put 1 of them into your hand. Discard the other card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Past Friends',
            game_text='This attack does 10 more damage for each Supporter card in your discard pile.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
