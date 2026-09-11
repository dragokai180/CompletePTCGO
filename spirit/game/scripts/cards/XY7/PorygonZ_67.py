from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='24dc9a73-f476-53e1-9544-cd2970ab7432',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name',
    display_name='Porygon-Z',
    searchable_by=['Porygon-Z', 'Stage 2', 'PorygonZ'],
    subtypes=['Stage 2'],
    collector_number=67,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    family_id=137,
    abilities=[
        Attack(
            title='Digital Reboot',
            game_text='Devolve as many of your Benched Pokémon as many times as you like. Put each Evolution card removed this way into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dazzle Blast',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."),
)
