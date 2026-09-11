from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f7e38224-bb82-5ac6-9637-2da585292109',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name',
    display_name='Talonflame',
    searchable_by=['Talonflame', 'Stage 2', 'Talonflame'],
    subtypes=['Stage 2'],
    collector_number=28,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Devastating Wind',
            game_text='Your opponent shuffles his or her hand into his or her deck and draws 4 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flare Blitz',
            game_text='Discard all Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
