from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6d8f7be4-8059-5bae-a73c-ff22f17bad24',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name',
    display_name='Hoopa',
    searchable_by=['Hoopa', 'Basic', 'Hoopa'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=720,
    abilities=[
        Ability(
            title='Scoundrel Guard',
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon-GX or Pokémon-EX.",
            passive=standard_passive("Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon-GX or Pokémon-EX."),
        ),
        Attack(
            title='Super Psy Bolt',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
