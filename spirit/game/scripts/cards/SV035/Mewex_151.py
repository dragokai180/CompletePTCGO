from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c7790cf4-98cf-5287-8417-fe8323f764e7',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name',
    display_name='Mew ex',
    searchable_by=['Mew ex', 'Basic', 'ex', 'Mewex'],
    subtypes=['Basic', 'ex'],
    collector_number=151,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=151,
    abilities=[
        Ability(
            title='Restart',
            game_text='Once during your turn, you may draw cards until you have 3 cards in your hand.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Genome Hacking',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
