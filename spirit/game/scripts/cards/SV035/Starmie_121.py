from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e80410c9-5f0a-5fb0-b1ae-035e8562445a',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name',
    display_name='Starmie',
    searchable_by=['Starmie', 'Stage 1', 'Starmie'],
    subtypes=['Stage 1'],
    collector_number=121,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    family_id=120,
    abilities=[
        Ability(
            title='Mysterious Comet',
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pokémon. If you placed any damage counters in this way, discard this Pokémon and all attached cards.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Speed Attack',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
