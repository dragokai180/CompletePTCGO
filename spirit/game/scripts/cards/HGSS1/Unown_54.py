from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34f24f94-5e43-571c-891b-8a08bff535af',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name',
    display_name='Unown',
    searchable_by=['Unown', 'Basic', 'Unown'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=201,
    abilities=[
        Ability(
            title='RETURN',
            game_text='Once during your turn, when you put Unown from your hand onto your Bench, you may return all Energy attached to 1 of your Pokémon to your hand.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Hidden Power',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
