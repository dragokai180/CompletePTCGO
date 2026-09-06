from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_ex
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.session.passives import Passive, carrier_pokemon


class RainbowDNAPassive(Passive):
    """This Pokémon can evolve into any Pokémon ex that evolves from Eevee."""

    def may_be_evolved_into(self, pokemon, carrier, evolution_card):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        if not is_pokemon_ex(evolution_card.archetype_id):
            return False
        return evolution_card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == "Eevee"


card = PokemonCardDef(
    guid="660d0ef4-ced3-5a93-8ed2-4b0baa9aca09",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eeveeex.Name",
    display_name="Eevee ex",
    searchable_by=["Eevee ex","Basic","ex","Tera","Eeveeex"],
    subtypes=["Basic","ex","Tera"],
    collector_number=75,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    family_id=133,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    passive=TeraRulePassive(),
    abilities=[
        Ability(
            title="Rainbow DNA",
            game_text="This Pokémon can evolve into any Pokémon ex that evolves from Eevee if you play it from your hand onto this Pokémon. (This Pokémon can't evolve during your first turn or the turn you play it.)",
            passive=RainbowDNAPassive(),
        ),
        Attack(
            title="Coruscating Quartz",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=200,
        ),
    ],
)
