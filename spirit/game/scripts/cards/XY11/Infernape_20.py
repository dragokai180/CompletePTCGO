from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='55552c18-25a5-59f5-ab65-5e844fb3ffd0',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name',
    display_name='Infernape',
    searchable_by=['Infernape', 'Stage 2', 'Infernape'],
    subtypes=['Stage 2'],
    collector_number=20,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name',
    family_id=390,
    abilities=[
        Attack(
            title='Flare Blitz',
            game_text='Discard all Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 2},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Flare Up',
            game_text='If you have fewer than 10 Fire Energy cards in your discard pile, this attack does nothing. Shuffle 10 Fire Energy cards from your discard pile into your deck.',
            cost={PokemonTypes.FIRE: 2},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
