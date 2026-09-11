from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='587cec75-bfd7-5142-8958-c34001cf4c75',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name',
    display_name='Charjabug',
    searchable_by=['Charjabug', 'Stage 1', 'Charjabug'],
    subtypes=['Stage 1'],
    collector_number=58,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name',
    family_id=736,
    abilities=[
        Ability(
            title='Battery',
            game_text="Once during your turn (before your attack), you may attach this card from your hand to 1 of your Vikavolt or Vikavolt-GX as a Special Energy card. This card provides 2 Lightning Energy only while it's attached to a Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Pierce',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
