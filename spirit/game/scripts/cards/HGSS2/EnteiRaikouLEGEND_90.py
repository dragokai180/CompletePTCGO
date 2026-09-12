from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2be6ea86-ac29-54a2-9ac2-0db2934aed45',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.EnteiRaikouLEGEND.Name',
    display_name='Entei & Raikou LEGEND',
    searchable_by=['Entei & Raikou LEGEND', 'LEGEND', 'EnteiRaikouLEGEND'],
    subtypes=['LEGEND'],
    collector_number=90,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=140,
    elements=[PokemonTypes.FIRE, PokemonTypes.LIGHTNING],
    stage=PokemonStage.LEGEND,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    weakness_types=[PokemonTypes.WATER, PokemonTypes.FIGHTING],
    family_id=243,
    abilities=[
        Attack(
            title='Detonation Spin',
            game_text='Discard a Fire Energy attached to Entei & Raikou LEGEND.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title='Thunder Fall',
            game_text="Discard all Energy attached to Entei & Raikou LEGEND. This attack does 80 damage to each Pokémon that has any Poké-Powers (both yours and your opponent's). This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
