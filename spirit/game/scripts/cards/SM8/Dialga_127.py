from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e036ce6b-d233-5115-b93f-95f50b4c0e73',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name',
    display_name='Dialga',
    searchable_by=['Dialga', 'Basic', 'Dialga'],
    subtypes=['Basic'],
    collector_number=127,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title='Turn Back Time',
            game_text="If your opponent's Active Pokémon is an evolved Pokémon, devolve it by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Power Blast',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
