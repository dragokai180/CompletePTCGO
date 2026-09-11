from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='27c100c4-04c4-5a4f-b6f5-3c300f41f680',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name',
    display_name='Alakazam-EX',
    searchable_by=['Alakazam-EX', 'Basic', 'EX', 'AlakazamEX'],
    subtypes=['Basic', 'EX'],
    collector_number=25,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=65,
    abilities=[
        Ability(
            title='Kinesis',
            game_text="When you play M Alakazam-EX from your hand to evolve this Pokémon, before it evolves, you may put 2 damage counters on your opponent's Active Pokémon and 3 damage counters on 1 of your opponent's Benched Pokémon.",
            passive=standard_passive("When you play M Alakazam-EX from your hand to evolve this Pokémon, before it evolves, you may put 2 damage counters on your opponent's Active Pokémon and 3 damage counters on 1 of your opponent's Benched Pokémon."),
        ),
        Attack(
            title='Suppression',
            game_text="Put 3 damage counters on each of your opponent's Pokémon that has any Energy attached to it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
